class Project < ActiveRecord::Base
  attr_accessible :name, :description, :start_date, :end_date, :owner_id
  has_and_belongs_to_many :users
  has_many :tickets

  validates_presence_of :name, :description, :start_date, :end_date
  
  validates :name,
            :length => { :minimum => 3, :maximum => 20 }

end
