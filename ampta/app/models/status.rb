class Status < ActiveRecord::Base
  attr_accessible :status_name
  has_many :tickets

  validates :status_name,
            :presence => true,
            :length => { :minimum => 3, :maximum => 20 }
end
